#!/bin/sh
# GIT_ASKPASS helper — supplies the persisted GitHub PAT to git without
# exposing it on command lines or in process listings.
# Usage: export GIT_ASKPASS=/home/z/my-project/scripts/git-askpass.sh
cat /home/z/my-project/.github_pat
