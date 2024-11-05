import pandas as pd
import matplotlib.pyplot as plt
import math
import torch

def visualize_feature_map(feature_map: torch.Tensor, channels_per_row: int = 8, cmap: str = 'viridis'):
    """
    可视化特征图的函数，将特征图以网格形式展示。

    Args:
        feature_map (torch.Tensor): 4D张量的特征图，形状为 (batch_size, channels, height, width)。
        需要从feature_maps中提取，比如
        two_conv_layer = list(feature_maps.keys())[1]
        feature_map = feature_maps[two_conv_layer]
        
        channels_per_row (int): 每行显示的通道数，默认值为8。
        cmap (str): 可视化的颜色映射方案，默认为 'viridis'。
    """
    num_channels = feature_map.shape[1]
    num_rows = math.ceil(num_channels / channels_per_row)

    plt.figure(figsize=(channels_per_row * 4, num_rows * 4))  # 设置图的大小

    for i in range(num_channels):
        plt.subplot(num_rows, channels_per_row, i + 1)
        plt.imshow(feature_map[0, i].cpu().detach().numpy(), cmap=cmap)  # 显示特征图
        plt.axis('off')
        plt.title(f"Channel {i}", fontsize=8)

    plt.tight_layout()
    plt.show()

# 使用方法示例
# visualize_feature_map(feature_map, channels_per_row=8, cmap='viridis')

def plot_metrics(csv_path, x_axis, y_axes):
    """
    从指定的CSV文件中绘制指定的多个指标曲线。

    参数:
    csv_path (str): CSV文件的路径
    x_axis (str): 横轴列名（如 "epoch" 或 "step"）
    y_axes (list): 纵轴列名的列表（如 ["train_dice_epoch", "val_dice_epoch", "train_loss_epoch"] 等）
    """
    # 读取CSV文件
    data = pd.read_csv(csv_path)

    # 检查列是否存在
    if x_axis not in data.columns:
        print(f"Error: '{x_axis}' column not found in CSV.")
        return
    for y_axis in y_axes:
        if y_axis not in data.columns:
            print(f"Error: '{y_axis}' column not found in CSV.")
            return
    
    # 提取指定的横轴数据
    x_data = data[x_axis]

    # 创建折线图
    plt.figure(figsize=(10, 6))
    for y_axis in y_axes:
        y_data = data[y_axis]
        plt.plot(x_data, y_data, marker='o', linestyle='-', label=y_axis)

    # 设置标题和标签
    plt.title(f"{', '.join(y_axes)} over {x_axis}")
    plt.xlabel(x_axis.capitalize())
    plt.ylabel("Values")
    plt.legend()
    plt.grid(True)
    plt.show()
