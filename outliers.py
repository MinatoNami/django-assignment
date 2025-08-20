import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RANSACRegressor
from sklearn.pipeline import make_pipeline


def read_csv(file_path):
    # Read CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Assuming the CSV file has columns named 'x' and 'y'
    points = list(zip(df['x'], df['y']))
    return points


def find_outliers_ransac(points, degree=2, residual_threshold=2.0):
    points = np.array(points)
    x = points[:, 0].reshape(-1, 1)
    y = points[:, 1]

    # Polynomial regression + RANSAC
    model = make_pipeline(
        PolynomialFeatures(degree),
        RANSACRegressor(residual_threshold=residual_threshold)
    )
    model.fit(x, y)

    inlier_mask = model.named_steps['ransacregressor'].inlier_mask_
    outlier_mask = ~inlier_mask

    inliers = points[inlier_mask]
    outliers = points[outlier_mask]

    # For plotting fitted curve
    x_plot = np.linspace(np.min(x), np.max(x), 500).reshape(-1, 1)
    y_plot = model.predict(x_plot)

    return inliers, outliers, x_plot, y_plot


def find_outliers_polynomial(points, degree=3):
    # Convert to arrays
    points = sorted(points)  # sort by x
    X = np.array([p[0] for p in points]).reshape(-1, 1)
    y = np.array([p[1] for p in points])

    # Polynomial regression
    poly = PolynomialFeatures(degree)
    X_poly = poly.fit_transform(X)

    model = LinearRegression()
    model.fit(X_poly, y)

    # Predictions
    y_pred = model.predict(X_poly)

    # Residuals
    residuals = y - y_pred
    threshold = 2 * np.std(residuals)

    # Outliers
    outliers = [(X[i][0], y[i])
                for i in range(len(y)) if abs(residuals[i]) > threshold]
    inliers = [(X[i][0], y[i])
               for i in range(len(y)) if abs(residuals[i]) <= threshold]

    return inliers, outliers, X, y_pred


file_path = "./coordinates.csv"
points = read_csv(file_path)

# Run both methods
inliers_poly, outliers_poly, X_poly, y_poly_pred = find_outliers_polynomial(
    points)
inliers_ransac, outliers_ransac, x_plot_ransac, y_plot_ransac = find_outliers_ransac(
    points, degree=3)

# Plotting
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Plot Polynomial Residual Method
axs[0].scatter([p[0] for p in points], [p[1]
               for p in points], color="lightgray", label="All Points")
axs[0].plot(X_poly, y_poly_pred, color="green", label="Polynomial Fit")
axs[0].scatter([p[0] for p in outliers_poly], [p[1]
               for p in outliers_poly], color="red", label="Outliers")
axs[0].set_title("Outlier Detection: Polynomial Residuals")
axs[0].set_xlabel("x")
axs[0].set_ylabel("y")
axs[0].legend()

# Plot RANSAC
axs[1].scatter([p[0] for p in points], [p[1]
               for p in points], color="lightgray", label="All Points")
axs[1].plot(x_plot_ransac, y_plot_ransac, color="blue", label="RANSAC Fit")
axs[1].scatter([p[0] for p in outliers_ransac], [p[1]
               for p in outliers_ransac], color="red", label="Outliers")
axs[1].set_title("Outlier Detection: RANSAC")
axs[1].set_xlabel("x")
axs[1].set_ylabel("y")
axs[1].legend()

plt.tight_layout()
plt.show()
