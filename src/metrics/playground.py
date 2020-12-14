import pickle
import cv2
import numpy as np
import time
from collections import defaultdict


class ToolBox:

    @staticmethod
    def play_video_from_seq(frames: list, title: str = None):

        for frame in frames:
            cv2.imshow(title if title else '', frame)
            if cv2.waitKey(50) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()

    @staticmethod
    def calculate_speed(ball_pos: list):
        speeds = defaultdict(list)
        scale_factor = 0.5
        for idx in range(len(ball_pos)):
            if idx == len(ball_pos) - 1:
                continue
            actual_x, actual_y = ball_pos[idx]
            next_x, next_y = ball_pos[idx + 1]
            vx = next_x - actual_x
            vy = next_y - actual_y
            v_mag = np.sqrt(vx**2 + vy**2) * scale_factor
            player = 'right' if vx > 0 else 'left'
            speeds[player].append(v_mag)
            print(f'[Frame {idx}]: Player: {player}, Velocity: {v_mag}')
            time.sleep(0.2)

        print(f"\n\nLeft player max speed: {np.max(speeds['left'])}")
        print(f"Right player max speed: {np.max(speeds['right'])}")
        print(f"Left player avg speed: {np.mean(speeds['left'])}")
        print(f"Right player avg speed: {np.mean(speeds['right'])}")


if __name__ == '__main__':

    with open('filename.pickle', 'rb') as handle:
        b = pickle.load(handle)
    ToolBox.calculate_speed(b['ball'])

    # frames = []
    # for frame_idx in range(len(b['ball'])):
    #     frame = np.zeros(b['shape'])
    #     frame = cv2.circle(frame, tuple(b['ball'][frame_idx]), 5, (255, 0, 255), -1)
    #     frames.append(frame)
    #
    # ToolBox.play_video_from_seq(frames)
