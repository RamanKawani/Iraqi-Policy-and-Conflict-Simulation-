def log_simulation_event(event):
    # Simple function to log events in a file (for debugging or tracking)
    with open('simulation_log.txt', 'a') as log_file:
        log_file.write(event + '\n')
