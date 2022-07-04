from constants import *
from utils import *
import git
import glob

clone_folder = "/tmp/yara-rules"


def parse_yara_rules(repo, file_pattern):
    mkdir_all(clone_folder)
    git.Git(clone_folder).clone(repo)
    print(repo, file_pattern)
    print(glob.glob(file_pattern, root_dir=clone_folder, recursive=True))


if __name__ == '__main__':
    for repo, file_pattern in YARA_RULES_GITHUB_REPOS.items():
        parse_yara_rules(repo, file_pattern)
