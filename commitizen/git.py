import os
from typing import NamedTuple, Callable
from tempfile import NamedTemporaryFile

from commitizen import cmd


def tag(tag: str):
    c = cmd.run(f"git tag {tag}")
    return c


def commit(message: str, args=""):
    f = NamedTemporaryFile("wb", delete=False)
    f.write(message.encode("utf-8"))
    f.close()
    c = cmd.run(f"git commit {args} -F {f.name}")
    os.unlink(f.name)
    return c


class Commit(NamedTuple):
    commit_hash: str
    author: str
    title: str
    message: str


def new_line_parser(commits: str) -> list:
    return commits.split("\n")


def full_commit_parser(commits: str) -> list:
    return commits.split("\ncommit ")


def get_commits(
    start: str,
    end: str = "HEAD",
    from_beginning: bool = False,
    pretty: str = "format:%s%n%b",
    parser: Callable = new_line_parser,
) -> list:

    c = cmd.run(f"git log --pretty={pretty} {start}...{end}")

    if from_beginning:
        c = cmd.run(f"git log --pretty={pretty} {end}")

    if not c.out:
        return []

    return parser(c.out)


def tag_exist(tag: str) -> bool:
    c = cmd.run(f"git tag --list {tag}")
    return tag in c.out


def is_staging_clean() -> bool:
    """Check if staing is clean"""
    c = cmd.run("git diff --no-ext-diff --name-only")
    c_cached = cmd.run("git diff --no-ext-diff --cached --name-only")
    return not (bool(c.out) or bool(c_cached.out))
