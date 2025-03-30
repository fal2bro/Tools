import cv2
import datetime

# カメラのデバイスID（適宜変更）
camera_id = 0  

# カメラを開く
cap = cv2.VideoCapture(camera_id)

# 解像度の設定
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)  # カメラのFPSを取得

# 撮影開始時の日時を取得し、ファイル名を生成
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"thermal_video_{timestamp}.avi"  # MP4にしたい場合は拡張子を .mp4 に変更

# 動画の保存設定（MP4なら 'mp4v'、AVIなら 'XVID'）
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(filename, fourcc, fps, (width, height))

print(f"Recording started: {filename}")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 動画に書き込む（カラーのまま）
    out.write(frame)

    # 画面に表示
    cv2.imshow('Thermal Camera', frame)

    # 'q' キーで終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 後処理
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Recording finished: {filename}")
