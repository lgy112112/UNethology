import pandas as pd
import matplotlib.pyplot as plt

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
