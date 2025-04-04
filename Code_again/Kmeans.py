import numpy as np
from sklearn.cluster import KMeans

# Dữ liệu
n = np.array([15,15,16,19,19,20,20,21,22,28,35,40,41,42,43,44,60,61,65]).reshape(-1, 1)

# Số cụm
K = 2

# Khởi tạo và huấn luyện mô hình KMeans
kmeans = KMeans(n_clusters=K, init=np.array([16, 22]).reshape(-1, 1), n_init=1)
kmeans.fit(n)

# Kết quả
centroids = kmeans.cluster_centers_.flatten()
clusters = kmeans.labels_

times = 1
print(f"Tâm cụm cuối cùng: {centroids}")
print(f"Phân cụm dữ liệu: {clusters}")
