"""
The template of the script for the machine learning process in game pingpong
"""

class MLPlay:
    def __init__(self, side):
        """
        Constructor

        @param side A string "1P" or "2P" indicates that the `MLPlay` is used by
               which side.
        """
        self.ball_served = False
        self.side = side
        self.speed = 0
        self.preBall = [0, 0]

    def nextBall(self, scene_info, X, Y, direction, speed, side):
        # dir : 0:右上, 1:右下, 2:左上, 3:左下    
        tempX = X
        tempY = Y
        for i in range(0, speed):
            if(direction == 0):
                tempX = tempX + 1
                tempY = tempY - 1
            elif(direction == 1):
                tempX = tempX + 1
                tempY = tempY + 1
            elif(direction == 2):
                tempX = tempX - 1
                tempY = tempY - 1
            elif(direction == 3):
                tempX = tempX - 1
                tempY = tempY + 1

            if(direction == 0):
                if(tempX >= 200):
                    return 195, tempY, 2
            elif(direction == 1):
                

        #     if(dire == 0):
        #         if(tempY <= 0):
        #             return tempX, 0, 1
        #         elif(tempX >= 200):
        #             return 195, tempY, 2
        #     elif(dire == 1):
        #         if(tempX >= 200):
        #             return 195, tempY, 3
        #     elif(dire == 2):
        #         if(tempY <= 0):
        #             return tempX, 0, 3
        #         elif(tempX <= 0):
        #             return 0, tempY, 0
        #     elif(dire == 3):
        #         if(tempX <= 0):
        #             return 0, tempY, 1

        #     for i in scene_info['bricks']:
        #         if(tempX>=i[0] and tempX<=(i[0]+25) and tempY>=i[1] and tempY<=(i[1]+10)):
        #             if(dire == 0):
        #                 if(abs(tempX - (i[0] + 25)) >= abs(tempY - (i[1]+10))):
        #                     return tempX, i[1]+10, 1
        #                 else:
        #                     return i[0]-5, tempY, 2
        #             elif(dire == 1):
        #                 if(abs(tempX - (i[0] + 25)) >= abs(tempY - (i[1]))):
        #                     return tempX, i[1]-5, 0
        #                 else:
        #                     return i[0]-5, tempY, 3
        #             elif(dire == 2):
        #                 if(abs(tempX - (i[0] + 25)) >= abs(tempY - (i[1]+10))):
        #                     return tempX, i[1]+10, 3
        #                 else:
        #                     return i[0] + 25, tempY, 0
        #             elif(dire == 3):
        #                 if(abs(tempX - (i[0] + 25)) >= abs(tempY - (i[1]))):
        #                     return tempX, i[1]-5, 2
        #                 else:
        #                     return i[0] + 25, tempY, 1
        # return tempX, tempY, dire

    def update(self, scene_info):
        """
        Generate the command according to the received scene information
        """
        if scene_info["status"] != "GAME_ALIVE":
            return "RESET"

        if not self.ball_served:
            self.ball_served = True
            return "SERVE_TO_LEFT"
        else:
            command = "NONE"

            speed = abs(scene_info['ball'][0] - self.preBall[0])
            X = scene_info['ball'][0]
            Y = scene_info['ball'][1]

            # dir : 0:右上, 1:右下, 2:左上, 3:左下
            direction = 0
            deltaBall = [0, 0]
            deltaBall[0] = scene_info['ball'][0] - self.preBall[0]
            deltaBall[1] = scene_info['ball'][1] - self.preBall[1]
            if(deltaBall[0] > 0 and deltaBall[1] < 0):
                direction = 0
            elif(deltaBall[0] > 0 and deltaBall[1] > 0):
                direction = 1
            elif(deltaBall[0] < 0 and deltaBall[1] < 0):
                direction = 2
            elif(deltaBall[0] < 0 and deltaBall[1] > 0):
                direction = 3

            print(scene_info['ball'])
            self.preBall = scene_info['ball']
            
            return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
