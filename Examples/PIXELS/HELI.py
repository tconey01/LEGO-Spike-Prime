from hub import port
import runloop
import motor_pair
import force_sensor
from hub import light
import color
from hub import light_matrix

async def main():
    
    force_sensor.force(port.F)
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    while True:  
        await runloop.sleep_ms(2000)

        if force_sensor.pressed(port.F):
            motor_pair.move(motor_pair.PAIR_1, 0, velocity=1110, acceleration=10)
            light.color(light.POWER, color.RED)
            light_matrix.show_image(37)

        
        else:
            motor_pair.move(motor_pair.PAIR_1, 0, velocity=0, acceleration=0)
            light.color(light.POWER, color.YELLOW)
            light_matrix.show_image(38)


        
        await runloop.sleep_ms(1000)

runloop.run(main())


