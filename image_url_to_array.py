import pandas as pd
import numpy as np
import urllib.request
from PIL import Image
import io
import csv
import sys
np.set_printoptions(threshold=sys.maxsize)



# def image_vectorizer (image):
#     # time.sleep(.5)
#     try:
#         # pd.options.display.max_seq_items = 1000000
#         request = urllib.request.Request(image, headers={'User-Agent': 'Mozilla/5.0'})
#         image = urllib.request.urlopen(request)
#         image = image.read()
#         image = Image.open(io.BytesIO(image))
#         arr = np.array(image, dtype='int64')
#         flat_arr = arr.ravel()
#         for i in flat_arr:
#             f.write(str(flat_arr.astype('uint64')) + " ")
#         # np.savetxt(f, flat_arr, fmt='%10.5f', delimiter=",", newline= "\n")
#             f.write("\n")
#         # return flat_arr
#         # f.write(" ".join(map(str, flat_arr)))
#
#     except urllib.error.URLError:
#         # return 0
#         f.write(0 + "\n")


def image_vectorizer (image):
    # time.sleep(.5)
    try:
        # pd.options.display.max_seq_items = 1000000
        request = urllib.request.Request(image, headers={'User-Agent': 'Mozilla/5.0'})
        image = urllib.request.urlopen(request)
        image = image.read()
        image =  bytearray(image)
        arr = np.array(image, dtype='int64')
        f.write(str(arr.astype('uint64')) + "\n")

        # print (len(arr))
        # np.savetxt(f, arr, fmt='%10.5f', delimiter=" ", newline= "\n")
        # f.write("\n")
    except urllib.error.URLError:
        return 0
        # f.write(0 + "\n")


pinterest_csv= ".\\csv_files\\new_pinterest.csv"
pinterest = pd.read_csv(pinterest_csv, encoding = "ISO-8859-1")

urls = pinterest['image_url'].tolist()
arrays = []

filename = "image_array_pickle.csv"

global f
# f = open(filename, "a", encoding="utf-8")
f = open(filename, "w")

cnt = 0
urls = urls[:10]
for url in urls:
    array = image_vectorizer(url)
    arrays.append(array)
    cnt = cnt + 1
    print(cnt)
    # if cnt > 10:
    #     break
f.close()


# df = pd.DataFrame({'image_array':arrays})
# print (df)
# df.to_pickle('image_array_pickle')