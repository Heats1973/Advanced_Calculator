from front_end_basic import Calculator_visuals
from front_end_advanced import Calculator_visuals_advanced

def switch_to_advanced():
    window_base.withdraw()
    window_advance.deiconify()

def back_to_main():
    window_advance.withdraw()
    window_base.deiconify()

window_base = Calculator_visuals(switch_to_advanced)
window_advance = Calculator_visuals_advanced(back_to_main)
window_advance.withdraw()

window_base.mainloop()