#!/bin/sh
# GIT_ASKPASS helper — supplies the persisted GitHub PAT to git without
# exposing it on command lines or in process listings.
# Uses the layered self-healing store (scripts/pat_store.sh).
exec /home/z/my-project/scripts/pat_store.sh get
