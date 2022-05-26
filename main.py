#!/usr/bin/env python3
import double_pendulum
import n_body
import gas_in_a_box
import sound_pulse

def main():

    # DOUBLE PENDULUM
    # -------------------------------------------------------------------------
    # double_pendulum.main(run_integrator=True)                        # works! 
    #                                                at least on my machine lol
    
    # DOUBLE PENDULUM
    # -------------------------------------------------------------------------
    # gas_in_a_box.main(run_integrator=True)                           # works!
    #
    # gas_in_a_box.live()                 # note: buggy, doesn't really work...
    
    # N-Body Gravity
    # -------------------------------------------------------------------------
    n_body.main(run_integrator=True)
    
    # SOUND PULSE       note: not my own code, I copied this from some-where...
    # -------------------------------------------------------------------------
    # sound_pulse.main()        

if __name__ == '__main__':
    main()
