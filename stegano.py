from stegano import lsb

secret = lsb.hide("potoku.png", "haii saya Raihan Tantowi")
secret.save("logo.png")
