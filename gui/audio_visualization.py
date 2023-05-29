import matplotlib.pyplot as plt

from logic.audio.audio import get_instance
from constants.paths import PATH_TO_AUDIO_PLOT_IMAGE


def get_audio_visualization():
    audio = get_instance().audio
    data = audio.get_array_of_samples()
    plt.figure(figsize=(20, 5))
    plt.plot(data, color='lightblue')
    plt.axis('off')
    plt.savefig(PATH_TO_AUDIO_PLOT_IMAGE, transparent=True)
