import os
import pytest
from selenium import webdriver
import subprocess
import time
import platform
import logging

logging.basicConfig(level=logging.INFO)


@pytest.fixture(scope="session")
def setup(request):
    """
    Fixture to set up a WebDriver instance for browser automation testing.

    Args:
        request (pytest.FixtureRequest): Provides access to configuration information.

    Returns:
        WebDriver: Instance of the WebDriver (in this case, Chrome).
    """
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    def teardown():
        driver.quit()

    request.addfinalizer(teardown)
    return driver


@pytest.fixture(scope="module", autouse=True)
def screen_recorder():
    output_dir = os.path.join(os.path.dirname(__file__), "recording")
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "output.mp4")

    logging.info(f"Output directory: {output_dir}")
    logging.info(f"Output file: {output_file}")

    # Define the ffmpeg command based on the OS
    if platform.system() == "Windows":
        ffmpeg_cmd = [
            'ffmpeg',
            '-f', 'gdigrab',  # Screen grab on Windows
            '-framerate', '30',  # Frames per second
            '-i', 'title=Fonu',  # Input source
            '-q:v', '10',  # Quality level (lower number is higher quality)
            output_file  # Output file
        ]
    elif platform.system() == "Linux":
        ffmpeg_cmd = [
            'ffmpeg',
            '-f', 'x11grab',  # Screen grab on Linux
            '-framerate', '30',  # Frames per second
            '-i', ':0.0',  # Input source (usually ':0.0')
            '-q:v', '10',  # Quality level (lower number is higher quality)
            output_file  # Output file
        ]
    else:
        raise RuntimeError(f"Screen recording is not supported on {platform.system()}")

    logging.info(f"ffmpeg command: {' '.join(ffmpeg_cmd)}")

    # Start the ffmpeg process
    ffmpeg_process = subprocess.Popen(ffmpeg_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Allow ffmpeg to start
    time.sleep(2)

    yield

    # Stop the ffmpeg process
    ffmpeg_process.terminate()

    # Ensure the ffmpeg process has terminated
    ffmpeg_process.wait()

    # Log the output and errors from the ffmpeg process
    stdout, stderr = ffmpeg_process.communicate()
    logging.info(f"ffmpeg stdout: {stdout.decode()}")
    logging.error(f"ffmpeg stderr: {stderr.decode()}")

    # Check if the output file was created
    if os.path.isfile(output_file):
        logging.info(f"Recording file created successfully: {output_file}")
    else:
        raise RuntimeError(f"Recording file was not created: {output_file}")
