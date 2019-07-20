from commitizen import git

LOG_OUTPUT = """commit dab7cc71fabe3b2721a43e71a87a6774f5cdaa55 (tag: refs/tags/v1.9.2)
Author: GitHub Action <action@github.com>
Date:   Sat Nov 23 10:21:16 2019 +0000

    bump: version 1.9.1 → 1.9.2

commit b13bbd5cd9b6a472d9bbec19481964f173320ce6
Author: Wei Lee <weilee.rx@gmail.com>
Date:   Sat Nov 23 05:20:44 2019 -0500

    fix(commands/check.py): --commit -msg-file is now a required argument

    * fix(commands/check.py): make --commit-msg-file a required argument for check command

    Currently, if --commit-msg-file is not provided, it throws exception

    * style(all): run ./script/lint

commit b9201b1fcdb8e6ec03a421cf9c7cc3435e189a84 (tag: refs/tags/v1.9.1)
Author: GitHub Action <action@github.com>
Date:   Sat Nov 23 10:18:51 2019 +0000

    bump: version 1.9.0 → 1.9.1

commit 149a5a9b1ac7f60302608a5e2959b46199b66c0f
Author: Wei Lee <weilee.rx@gmail.com>
Date:   Sat Nov 23 05:18:16 2019 -0500

    fix(cz/exceptions): exception AnswerRequiredException not caught (#89)

    * fix(cz/exceptions): Fix AnswerRequiredException not caught

    inherit CzException

    * style(all): run ./script/lint

commit db1c4bf602212a5bf8899711f96cd23cede57391
Merge: 90d3568 65f837d
Author: Santiago <santiwilly@gmail.com>
Date:   Fri Nov 22 19:59:08 2019 +0100

    Merge pull request #88 from Woile/77-github-actions

    77 GitHub actions

commit 65f837dab506e3aee825a6c12da8156e2f5509fb (refs/remotes/origin/77-github-actions)
Author: santiago fraire <santiwilly@gmail.com>
Date:   Fri Nov 22 19:56:23 2019 +0100

    docs: updated changelog

commit 033c8d1d80a575c51ad4e92b21ec6b7ba0f52357
Author: santiago fraire <santiwilly@gmail.com>
Date:   Fri Nov 22 19:56:08 2019 +0100

    ci: publish with github secret
"""


def test_full_commit_parser_separates_properly():
    commits = git.full_commit_parser(LOG_OUTPUT)
    import ipdb; ipdb.set_trace()
    assert len(commits) == 7
