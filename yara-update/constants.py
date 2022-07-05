YARA_RULES_GITHUB_REPOS = {
    "https://github.com/Neo23x0/signature-base": {
        "pattern": ["yara/*.yar"], "path": "signature-base"},
    "https://github.com/spyre-project/spyre": {
        "pattern": ["example-config/*.yara"], "path": "spyre"},
    "https://github.com/mandiant/red_team_tool_countermeasures": {
        "pattern": ["rules/**/*.yar"], "path": "red_team_tool_countermeasures"},
    "https://github.com/volexity/threat-intel": {
        "pattern": ["**/*.yar"], "path": "threat-intel"},
    "https://github.com/Yara-Rules/rules": {
        "pattern": ["**/*.yar"], "path": "rules"}
}

RULE_FILE_NAME_EXCLUSION = [
    "_win_", "windows", "win7", "win8", "win2k", "win2000", "winxp", "winnt", "deprecated", "android"]
RULE_CONTENT_EXCLUSION = [
    "c:\\\\", "d:\\\\", "e:\\\\", "f:\\\\", "microsoft", "win7", "win8", "win2k", "win2000", "winxp", "winnt", ".exe",
    "windows", "deprecated", "android", "msie"]
