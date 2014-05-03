

if __name__ == '__main__':
    
    from Config import Config
    from Robot import Robot
    robot = Robot(Config())
    while True :
        robot.actuar();
