import urllib

i = 0
while i < 1000:
    urllib.urlretrieve(
        "http://www.lastweektickets.com/image.php?ssw=ef4nci2t3ggod2pm0spthdnur4",
        "./examples_raw/{0:03d}.png".format(i)
    )
    i += 1
