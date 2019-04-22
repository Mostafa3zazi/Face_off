#OpenCV module
import cv2
#os module for reading training data directories and paths
import os
#numpy to convert python lists to numpy arrays as it is needed by OpenCV face recognizers
import numpy as np

from detectFace import detect_face

# this function will read all persons' training images, detect face from each image
# and will return two lists of exactly same size, one list
# of faces and another list of labels for each face
def prepare_training_data(data_folder_path):
    # ------STEP-1--------
    # get the directories (one directory for each subject) in data folder
    dirs = os.listdir(data_folder_path)
    ##print (dirs)
    
    # list to hold all subject faces
    faces = []
    # list to hold labels for all subjects
    labels = []

    # let's go through each directory and read images within it
    for dir_name in dirs:

        # our subject directories start with letter 's' so
        # ignore any non-relevant directories if any
        if not dir_name.startswith("s"):
            continue;

        # ------STEP-2--------
        # extract label number of subject from dir_name
        # format of dir name = slabel
        # , so removing letter 's' from dir_name will give us label
        label = int(dir_name.replace("s", ""))

        # build path of directory containing images for current subject subject
        # sample subject_dir_path = "training-data/s1"
        subject_dir_path = data_folder_path + "/" + dir_name

        # get the images names that are inside the given subject directory
        subject_images_names = os.listdir(subject_dir_path)

        # ------STEP-3--------
        # go through each image name, read image,
        # detect face and add face to list of faces
        i=0
        for image_name in subject_images_names:

            # ignore system files like .DS_Store
            if image_name.startswith("."):
                continue;

            # build image path
            # sample image path = training-data/s1/1.pgm
            image_path = subject_dir_path + "/" + image_name

            # read image
            image = cv2.imread(image_path)

            # display an image window to show the image
            showGray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            ##cv2.imshow("Training on image...", showGary)
            cv2.waitKey(5)

            # detect face
            face, rect = detect_face(image)

        # ------STEP-4--------
        # we will ignore faces that are not detected
            if face is not None:
                # add face to list of faces
                i+=1
                faces.append(face)
                ##cv2.imshow("result",face)
                ##cv2.imwrite('C:/Users/Unknown/Desktop/faceoff'+'/lable{0}Number{1}.jpg'.format(label,i),face)
                cv2.waitKey(5)
                # add label for this face
                labels.append(label)

        cv2.destroyAllWindows()
        cv2.waitKey(1)
        cv2.destroyAllWindows()

    return faces, labels

##faces,labels=prepare_training_data("C:/Users/Unknown/Desktop/faceoff")
##print(labels)
