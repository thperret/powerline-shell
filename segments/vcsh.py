import os

def add_vcsh_segment():
    vcsh_repo_name = os.getenv('VCSH_REPO_NAME')
    if vcsh_repo_name is None:
        return

    bg = Color.VCSH_BG
    fg = Color.VCSH_FG
    powerline.append(' %s ' % vcsh_repo_name, fg, bg)

add_vcsh_segment()
