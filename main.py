import time

if __name__=="__main__":
    main_screen.draw()
    while True:
        new_tab_number = main_screen.handler()
        if new_tab_number != main_screen.current_tab_number:
            main_screen.current_tab_number = new_tab_number
            main_screen.draw()
            for i, tab in enumerate([tab1, tab2, tab3]):
                if i == main_screen.current_tab_number:
                    tab.draw()
                    tab.draw_error()
        
        tab2.handler()
