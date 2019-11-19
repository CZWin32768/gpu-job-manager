import os
import argparse
import sys
import yaml
import logging
import subprocess
import threading
import time


logging.basicConfig(
  format = '%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
  datefmt = '%m/%d/%Y %H:%M:%S',
  level = logging.INFO)
logger = logging.getLogger(__name__)


def target_func(command, log_path, device):
  with open(log_path, "w") as fp:
    subprocess.run("CUDA_VISIBLE_DEVICES=%d %s" % (device, command), shell=True, stdout=fp, stderr=fp)


def job_generator(job):
  
  param_dicts = []
  params = job["params"]
  max_deep = len(params)
  temp_dict = {param["name"]:None for param in params}

  def _param_search(deep):
    if deep >= max_deep:
      logger.info(str(temp_dict))
      param_dicts.append({key:temp_dict[key] for key in temp_dict})
      return
    param = params[deep]
    for value in param["values"]:
      temp_dict[param["name"]] = value
      _param_search(deep + 1)

  logger.info("Parsing Jobs...")
  _param_search(0)
  logger.info("Finding %d jobs to run..." % len(param_dicts))

  job = job["job_template"]
  for param_dict in param_dicts:
    name = job["name"]
    command = job["command"][-1]
    for key, value in param_dict.items():
      name = name.replace("{%s}" % key, value)
      command = command.replace("{%s}" % key, value)
    yield name, command


def main(args):
  with open(args.i) as fp:
    job_config = yaml.load(fp)
  
  # parse code dir
  config_dir = os.path.dirname(args.i)
  code_dir = job_config["code"]["local_dir"]
  if code_dir.startswith("$CONFIG_DIR/"):
    code_dir = os.path.join(config_dir, code_dir[len("$CONFIG_DIR/"):])
  else: raise NotImplementedError
  logger.info("code_dir is set as %s" % code_dir)
  assert os.path.isdir(code_dir)
  os.chdir(code_dir)
  logger.info("Current dir is set as %s" % os.curdir)

  # doing jobs
  job = job_config["search"]
  # for name, command in job_generator(job):
  #   logger.info(name)
  #   logger.info(command)
  job_iter = job_generator(job)
  threads = [None] * args.ngpu
  has_job = True
  while has_job:
    for i, thread in enumerate(threads):
      if thread is None or not thread.is_alive():
        try:
          next_job_name, next_job_command = next(job_iter)
        except StopIteration:
          has_job = False
          break
        logger.info("Start running job: %s on %d-th GPU" % (next_job_name, i))
        logger.info("Command: %s" % next_job_command)
        log_path = os.path.join(args.logdir, next_job_name)
        thread = threading.Thread(
          target=target_func, args=(next_job_command, log_path, i))
        threads[i] = thread
        thread.start()
    time.sleep(5)

  for thread in threads:
    if thread != None: thread.join()


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument(
    "-i", required=True, type=str, help="input yaml file")
  parser.add_argument("--ngpu", required=True, type=int)
  parser.add_argument("--logdir", type=str, default="./log")
  args = parser.parse_args()
  assert os.path.isfile(args.i)
  args.logdir = os.path.abspath(args.logdir)
  os.makedirs(args.logdir, exist_ok=True)
  main(args)
