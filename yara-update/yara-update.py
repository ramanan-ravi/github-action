from constants import *
from utils import *
import git
import glob
import yara
import shutil

clone_folder = "/tmp/yara-rules"
output_rule_file = "/tmp/filescan.yar"


def parse_yara_rules(repo, file_patterns):
    repo_path = os.path.join(clone_folder, file_patterns["path"])
    if not os.path.isdir(repo_path):
        git.Git(clone_folder).clone(repo)
    rule_files = []
    for file_pattern in file_patterns["pattern"]:
        file_names = glob.glob(file_pattern, root_dir=repo_path, recursive=True)
        for file_name in file_names:
            if any(exclusion in str(file_name).lower() for exclusion in RULE_FILE_EXCLUSION):
                continue
            rule_files.append(file_name)
    with open(output_rule_file, "a") as output_file:
        for file_name in rule_files:
            try:
                rule_file_name = os.path.join(repo_path, file_name)
                yara.compile(filepath=rule_file_name)
                # It is a valid yara rule file
                with open(rule_file_name, 'r') as file:
                    data = file.read()
                    output_file.write(data)
            except:
                pass


if __name__ == '__main__':
    mkdir_all(clone_folder)
    for repo, file_patterns in YARA_RULES_GITHUB_REPOS.items():
        try:
            parse_yara_rules(repo, file_patterns)
        except Exception as e:
            print(e)
    shutil.rmtree(clone_folder)
