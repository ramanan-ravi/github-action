from constants import *
from utils import *
import git

clone_folder = "/tmp/yara-rules"


def parse_yara_rules(repo):
    mkdir_all(clone_folder)
    git.Git(clone_folder).clone(repo)


if __name__ == '__main__':
    for repo in YARA_RULES_GITHUB_REPOS:
        parse_yara_rules(repo)
    print(os.listdir(clone_folder))
