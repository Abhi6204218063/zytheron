from modules.diffusion_generative_model import diffusion_generate


def generate_million_library():

    library = []

    batch = 10000

    for i in range(100):  # 100 × 10k = 1,000,000

        molecules = diffusion_generate(batch)

        library.extend(molecules)

    return library
