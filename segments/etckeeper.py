import subprocess

def add_etckeeper_segment(powerline):
    try:
        p = subprocess.Popen(['sudo', 'etckeeper', 'unclean'],
                             stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    except OSError:
        return

    pdata = p.communicate()
    if p.returncode == 0:
        powerline.append(' etckeeper ', Color.ETC_DIRTY_BG, Color.ETC_DIRTY_FG)
