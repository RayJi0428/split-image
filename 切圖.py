import cv2
import numpy as np
import json
import sys
import os

if len(sys.argv) == 1:
    # test
    json_file = f'{os.getcwd()}\\jp1_font.fnt'
    png_file = f'{os.getcwd()}\\jp1_font.png'
else:
    if '.png' in sys.argv[1]:
        png_file = sys.argv[1]
        json_file = sys.argv[2]
    else:
        png_file = sys.argv[2]
        json_file = sys.argv[1]

output_dir = os.path.dirname(png_file) + "\\output\\"
# 建folder
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# 讀取json(增加UTF-8解決db檔案問題)
with open(json_file, "r", encoding="UTF-8") as f:
    json_data = json.load(f)

# 讀取png
# IMREAD_COLOR(預設 BGR)
# IMREAD_GRAYSCALE(灰階)
# IMREAD_UNCHANGED(alpha BGRA)
img = cv2.imread(png_file, cv2.IMREAD_UNCHANGED)  # bgra

if 'frames' in json_data:
    # 切圖
    for name in json_data['frames']:
        frame_data = json_data['frames'][name]
        x = frame_data['x']  # 位於spritesheet x座標
        y = frame_data['y']  # 位於spritesheet y座標
        w = frame_data['w']  # 位於spritesheet 寬
        h = frame_data['h']  # 位於spritesheet 高
        ox = frame_data['offX']  # 位於spritesheet 裁減區和原圖x偏移量
        oy = frame_data['offY']  # 位於spritesheet 裁減區和原圖y偏移量
        sw = frame_data['sourceW']  # 原圖寬度(含透明區)
        sh = frame_data['sourceH']  # 原圖高度(含透明區)

        # 從spritesheet切出目標
        copy = img[y:y+h, x:x+w]

        # 將目標版面以中心擴展為原始圖尺寸
        dst = cv2.copyMakeBorder(copy, oy, sh-h-oy, ox,
                                 sw-w-ox, cv2.BORDER_CONSTANT)

        # 另存圖片
        # cv2.imwrite(output_dir + name + '.png', dst)
        # 中文檔名儲存會有問題，改用imencode代替
        # https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/356918/
        cv2.imencode('.png', dst)[1].tofile(output_dir + name + '.png')
elif 'SubTexture' in json_data:
    # 切圖
    idx = 0
    for frame_data in json_data['SubTexture']:
        name = frame_data['name']  # 名稱
        x = frame_data['x']  # 位於spritesheet x座標
        y = frame_data['y']  # 位於spritesheet y座標
        w = frame_data['width']  # 位於spritesheet 寬
        h = frame_data['height']  # 位於spritesheet 高
        ox = 0  # 位於spritesheet 裁減區和原圖x偏移量
        oy = 0  # 位於spritesheet 裁減區和原圖y偏移量

        # 從spritesheet切出目標
        copy = img[y:y+h, x:x+w]

        # __dbTextures/top_info/圖層_3_0 檔名不可包含/
        name = name.replace('/', '_')
        name = name.replace(' ', '_')
        # 另存圖片
        # cv2.imwrite(output_dir + name + '.png', copy)
        # 中文檔名儲存會有問題，改用imencode代替
        # https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/356918/
        cv2.imencode('.png', copy)[1].tofile(output_dir + name + '.png')
elif 'mc' in json_data:
    # 切圖
    idx = 0
    for name in json_data['res']:
        frame_data = json_data['res'][name]
        x = frame_data['x']  # 位於spritesheet x座標
        y = frame_data['y']  # 位於spritesheet y座標
        w = frame_data['w']  # 位於spritesheet 寬
        h = frame_data['h']  # 位於spritesheet 高
        ox = 0  # 位於spritesheet 裁減區和原圖x偏移量
        oy = 0  # 位於spritesheet 裁減區和原圖y偏移量

        # 從spritesheet切出目標
        copy = img[y:y+h, x:x+w]

        # __dbTextures/top_info/圖層_3_0 檔名不可包含/
        name = name.replace('/', '_')
        name = name.replace(' ', '_')
        # 另存圖片
        # cv2.imwrite(output_dir + name + '.png', copy)
        # 中文檔名儲存會有問題，改用imencode代替
        # https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/356918/
        cv2.imencode('.png', copy)[1].tofile(output_dir + name + '.png')

input("done!")
