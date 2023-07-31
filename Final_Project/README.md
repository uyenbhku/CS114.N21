# Final Project: GARBAGE CLASSIFICATION

## By team: NSFW

## Project Description
This is a garbage classification project. To accomplish this project, we used the TensorFlow framework and Scikit-learn library.

This is not a project for production and is only meant to conduct some experiments to evaluate and compare the performance of some Machine Learning models for this type of problem. However, we still provide our trained models that can easily be reused for production! 

## Repository tree:
```bash
Final_Project
├── dataset/
│── experiments/
│── model_serving/
│   ├── VGG16_serving.ipynb
│   └── ResNet50_serving.ipynb
│── preprocess_script/
│   ├── constants.py
│   └── resize.py
│── Final_Report.pdf
└── README.md
 ```

- `dataset` will tell you about the information of the dataset we use
- `experiments` includes:
   - about 15 notebooks that can tell you more detail about the performance of each model,
   - our trained models (Note: ResNet50 models are not available because of large size)
- `model_serving` includes two ready-to-use notebooks that you can have fun with your images
- `preprocess_script` includes Python scripts that we used to preprocess our images. We modified a bit from the scripts that the Trashnet author provided due to outdated packages.
- `Final_Report.pdf` will give you some more information in Vietnamese.
