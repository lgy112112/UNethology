[中文版本](README.zh.md)

## UNethology 🐚: Exploring UNet Applications 🧬

Welcome to **UNethology**, a repository dedicated to showcasing the versatility of UNet, a powerful deep learning architecture for image segmentation and beyond. In this repository, I delve into my journey of utilizing UNet to tackle a variety of problems, demonstrating its adaptability and effectiveness in various domains.

**Recent Updates:** 🏆

* **November 5, 2024:** [A new notebook](Brain_Tumor_Segmentation_UNet/how_to_visualize_features_map.ipynb) guiding you how to visualize feature map via hook function.

![alt text](image.png)

* **November 4, 2024:** Introduced a comprehensive Jupyter notebook detailing the training process of UNet for brain tumor segmentation on MRI images. This notebook covers data loading, dataset and dataloader creation, model setup with MONAI's BasicUNet, and the training pipeline using PyTorch Lightning. The project highlights the integration of UNet with advanced medical imaging frameworks for precise segmentation tasks. You can get data via [Brain_Tumor_Segmentation_UNet/data_get.ipynb](Brain_Tumor_Segmentation_UNet/data_get.ipynb), 
train in [Brain_Tumor_Segmentation_UNet/train.ipynb](Brain_Tumor_Segmentation_UNet/train.ipynb). This project is the most detailed-detailed-ever one including how to assess model, plotting results. I will update this part in the following days.
 
* **May 6, 2024:** Added a new project demonstrating UNet for medical image segmentation on the SMU Dataset. Check out the notebook: [SMU Dataset: UNet for Medical Image Segmentation](https://www.kaggle.com/code/liaoguoying/smu-dataset-dl-update-with-new-dataset). In this project, I use smp to construct ViT-based UNet to compare with ResUNet. Plus, [a novel loss function](https://github.com/lgy112112/DiceCELossWithKL) is applied.

* **April 15, 2024:** Successfully employed UNet to tackle a regression prediction challenge on Kaggle, specifically [predicting the age of abalones](https://www.kaggle.com/competitions/playground-series-s4e4). See the Kaggle notebook: [UNethology: Predict Age with UNet???](https://www.kaggle.com/code/liaoguoying/unethology-predict-age-with-unet).

**Stay tuned for more UNet adventures!** 🚀

As I continue my exploration of UNet's capabilities, I'll be adding more projects and insights to this repository. Feel free to follow along and join me on this exciting journey of UNet-powered problem-solving! 🤓

**Projects:**

* **Brain Tumor Segmentation on MRI Images:** A detailed walkthrough of setting up UNet for segmenting brain tumors in MRI scans, leveraging PyTorch Lightning and MONAI for efficient training and evaluation.
* **SMU Dataset: UNet for Medical Image Segmentation** - Demonstrates UNet for segmenting medical images from the SMU Dataset, showcasing its potential in medical image analysis.
* **UNethology: Predict Age with UNet???** - A Kaggle notebook demonstrating how UNet can be adapted for regression prediction tasks, specifically predicting the age of abalones.

Please note that the links provided may not be accessible due to network issues or the validity of the URLs. If you encounter any issues, please verify the URLs and try accessing them again. If the problem persists, it might be related to temporary network fluctuations or the specific platform's availability.

