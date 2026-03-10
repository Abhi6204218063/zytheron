def select_candidates(screen_results):

    screen_results.sort(key=lambda x: x[1])

    return screen_results[:5]
