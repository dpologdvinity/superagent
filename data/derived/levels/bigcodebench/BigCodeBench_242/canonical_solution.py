import cv2
import matplotlib.pyplot as plt

def task_func(image_path, kernel_size):
    """
    Applies a blur effect to an image using a specified kernel size, then visualizes both the original and blurred images side by side.

    Parameters:
    - image_path (str): The file path to the input image.
    - kernel_size (int): The size of the kernel used for blurring. Must be a positive integer.

    Returns:
    - tuple: A tuple containing a numpy.ndarray of the blurred image, and two matplotlib.axes.Axes objects for the plots of the original and blurred images.

    Raises:
    - FileNotFoundError: If the specified image file does not exist.
    - ValueError: If kernel_size is not a positive integer.

    Requirements:
    - opencv-python (cv2) for image processing.
    - matplotlib.pyplot for plotting images.

    Example:
    >>> dummy_img_path = "image.jpg"
    >>> np.random.seed(42)
    >>> dummy_img = np.random.randint(0, 255, (20, 20, 3), dtype=np.uint8)
    >>> cv2.imwrite(dummy_img_path, dummy_img)
    True
    >>> blurred_img, ax_original, ax_blurred = task_func('image.jpg', 5) # The function returns the blurred image array, and axes objects with titles 'Original' and 'Blurred' for the original and blurred images, respectively.
    >>> os.remove(dummy_img_path)
    """
    if kernel_size <= 0 or not isinstance(kernel_size, int):
        raise ValueError("kernel_size must be a positive integer")
    
    try:
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"No image found at {image_path}")
    except FileNotFoundError as e:
        raise e

    blurred_image = cv2.blur(image, (kernel_size, kernel_size))

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), ax1.set_title('Original')
    ax1.set_xticks([]), ax1.set_yticks([])
    ax2.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB)), ax2.set_title('Blurred')
    ax2.set_xticks([]), ax2.set_yticks([])
    # plt.show()

    return blurred_image, ax1, ax2
