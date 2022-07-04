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

RULE_FILE_EXCLUSION = ["_win_"]