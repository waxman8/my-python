import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Generate some sample data
np.random.seed(1)
X = 5 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

print(f"....{np.random.randn(2, 1)}")
# print(f"X={X}")
# print(f"Y={y}")

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)


# print(f"X-train={X_train}")
print(f"X-test={X_test}")
# print(f"Y-train={y_train}")
# print(f"Y-test={y_test}")

# Create a linear regression model
model = LinearRegression()

# Fit the model to the training data
model.fit(X, y)

# Make predictions on the test data
y_pred = model.predict(X_test)

mdv_pred = model.predict([[2],[3],[4]])
print(mdv_pred)

# Visualize the results
plt.scatter(X_test, y_test, label='Actual Data')
plt.scatter(X_test, y_pred, label='Predicted Data')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Linear Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()

# Print the model's coefficients
print("Intercept (theta_0):", model.intercept_[0])
print("Slope (theta_1):", model.coef_[0][0])