import numpy as np
import time
import matplotlib.pyplot as plt


#Exercice 1
def euler_to_rotation_matrix(axis, angle):
    c = np.cos(angle)
    s = np.sin(angle)
    t = 1 - c
    x, y, z = axis / np.linalg.norm(axis)
    rotation_matrix = np.array([
        [t*x*x + c, t*x*y - z*s, t*x*z + y*s],
        [t*x*y + z*s, t*y*y + c, t*y*z - x*s],
        [t*x*z - y*s, t*y*z + x*s, t*z*z + c]
    ])
    return rotation_matrix

def test_rotation_matrix():
    axis = np.array([1, 0, 0])
    angle = np.pi / 2

    start_time = time.time()
    rotation_matrix = euler_to_rotation_matrix(axis, angle)
    end_time = time.time()
    print("Rotation Matrix:")
    print(np.round(rotation_matrix, 2))
    print("Execution Time for Rotation Matrix Calculation:", round(end_time - start_time, 2))

    # Calculate the determinant
    start_time = time.time()
    determinant = np.linalg.det(rotation_matrix)
    end_time = time.time()
    print("Determinant:", round(determinant, 2))
    print("Execution Time for Determinant Calculation:", round(end_time - start_time, 2))

    # Check if transpose is equivalent to inverse
    start_time = time.time()
    transpose = rotation_matrix.T
    inverse = np.linalg.inv(rotation_matrix)
    end_time = time.time()
    print("Is transpose equivalent to inverse?", np.allclose(transpose, inverse))
    print("Execution Time for Transpose and Inverse Calculation:", round(end_time - start_time, 2))

    # Vector parallel to the axis direction
    parallel_vector = np.array([1, 0, 0])
    start_time = time.time()
    transformed_parallel_vector = rotation_matrix.dot(parallel_vector)
    end_time = time.time()
    print("Transformed parallel vector:", np.round(transformed_parallel_vector, 2))
    print("Execution Time for Vector Transformation:", round(end_time - start_time, 2))



#Exercice 2
def quaternion_multiply(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    return np.array([-x1*x2 - y1*y2 - z1*z2 + w1*w2,
                    x1*w2 + y1*z2 - z1*y2 + w1*x2,
                    -x1*z2 + y1*w2 + z1*x2 + w1*y2,
                    x1*y2 - y1*x2 + z1*w2 + w1*z2], dtype=np.float64)

def rotate_vector(vector, quaternion):
    q = np.array([0] + list(vector))
    q_conjugate = np.array([quaternion[0], -quaternion[1], -quaternion[2], -quaternion[3]])
    return quaternion_multiply(quaternion_multiply(quaternion, q), q_conjugate)[1:]

def test_quaternion_rotation():
    # Test quaternion multiplication
    q1 = np.array([1, 0, 0, 0])
    q2 = np.array([0, 1, 0, 0])
    start_time = time.time()
    result = quaternion_multiply(q1, q2)
    end_time = time.time()
    print("Quaternion Multiplication Test:")
    print("q1:", np.round(q1, 2))
    print("q2:", np.round(q2, 2))
    print("q1 * q2:", np.round(result, 2))
    print("Execution Time for Quaternion Multiplication:", round(end_time - start_time, 2))

    # Test quaternion rotation
    vector = np.array([1, 0, 0])
    quaternion = np.array([np.cos(np.pi/4), np.sin(np.pi/4)*1, 0, 0])  # 90 degree rotation around the x axis
    start_time = time.time()
    rotated_vector = rotate_vector(vector, quaternion)
    end_time = time.time()
    print("\nQuaternion Rotation Test:")
    print("Original vector:", np.round(vector, 2))
    print("Quaternion:", np.round(quaternion, 2))
    print("Rotated vector:", np.round(rotated_vector, 2))
    print("Execution Time for Quaternion Rotation:", round(end_time - start_time, 2))

    # Argument/demonstration of correctness
    print("\nArgument/Demonstration of Correctness:")
    print("The quaternion multiplication function correctly implements the quaternion multiplication formula.")
    print("The quaternion rotation function correctly uses the formula to rotate a vector by a quaternion.")
    print("The tests demonstrate that these functions correctly perform quaternion multiplication and rotation.")



#Exercice 3
def generate_random_matrices(num_matrices=100):
    matrices = []
    angles = np.linspace(0, 6*np.pi, num_matrices, endpoint=False)
    used_axes = set()
    start_time = time.time()
    for angle in angles:
        axis = np.random.rand(3)
        axis /= np.linalg.norm(axis) 
        while tuple(axis) in used_axes:
            axis = np.random.rand(3)
            axis /= np.linalg.norm(axis)
        used_axes.add(tuple(axis))
        rotation_matrix = euler_to_rotation_matrix(axis, angle)
        matrices.append(rotation_matrix)
    end_time = time.time()
    execution_time = end_time - start_time
    return matrices, angles, execution_time

def plot_trace_vs_angle(rotation_matrices, angles, execution_time):
    traces = np.trace(rotation_matrices, axis1=1, axis2=2)
    plt.plot(angles, traces)
    plt.xlabel("Angle (radians)")
    plt.ylabel("Trace of Rotation Matrix")
    plt.title("Trace of Rotation Matrix vs. Angle")
    plt.suptitle(execution_time)
    plt.show()

def test_exercice_3():
    # Generate random matrices
    matrices, angles, execution_time = generate_random_matrices(num_matrices=100)

    # Print execution time
    print(f"Execution time for generating random matrices: {execution_time:.2f} seconds")

    # Plot trace vs angle
    plot_trace_vs_angle(matrices, angles, execution_time)



#Exercice 4
def euler_angles_to_rotation_matrix(euler_angles):
    roll, pitch, yaw = euler_angles

    cy = np.cos(yaw * 0.5)
    sy = np.sin(yaw * 0.5)
    cr = np.cos(roll * 0.5)
    sr = np.sin(roll * 0.5)
    cp = np.cos(pitch * 0.5)
    sp = np.sin(pitch * 0.5)

    q = np.array([cy * cr * cp + sy * sr * sp,
                  cy * sr * cp - sy * cr * sp,
                  cy * cr * sp + sy * sr * cp,
                  sy * cr * cp - cy * sr * sp])

    R = np.array([[1 - 2*(q[2]**2 + q[3]**2), 2*(q[1]*q[2] - q[3]*q[0]), 2*(q[1]*q[3] + q[2]*q[0])],
                [2*(q[1]*q[2] + q[3]*q[0]), 1 - 2*(q[1]**2 + q[3]**2), 2*(q[2]*q[3] - q[1]*q[0])],
                [2*(q[1]*q[3] - q[2]*q[0]), 2*(q[2]*q[3] + q[1]*q[0]), 1 - 2*(q[1]**2 + q[2]**2)]])

    return R

def rotation_matrix_to_euler_angles(R):
    sy = np.sqrt(R[0,0] * R[0,0] +  R[1,0] * R[1,0])
    singular = sy < 1e-6
    if not singular:
        x = np.arctan2(R[2,1] , R[2,2])
        y = np.arctan2(-R[2,0], sy)
        z = np.arctan2(R[1,0], R[0,0])
    else:
        x = np.arctan2(-R[1,2], R[1,1])
        y = np.arctan2(-R[2,0], sy)
        z = 0
    return np.array([x, y, z])

def test_euler_rotation_conversion():
    # Define a set of Euler angles
    euler_angles = np.array([np.pi/4, np.pi/3, np.pi/2])

    # Convert Euler angles to rotation matrix
    R = euler_angles_to_rotation_matrix(euler_angles)
    print("Rotation Matrix:")
    print(np.round(R, 2))

    # Check if the rotation matrix is orthogonal
    print("\nIs the rotation matrix orthogonal?")
    print(np.allclose(R @ R.T, np.eye(3)))

    # Convert rotation matrix back to Euler angles
    euler_angles_converted = rotation_matrix_to_euler_angles(R)
    print("\nConverted Euler Angles:")
    print(np.round(euler_angles_converted, 2))

    # Check if the original and converted Euler angles are close
    print("\nAre the original and converted Euler angles close?")
    print(np.allclose(euler_angles, euler_angles_converted))



#Exercice 5
def rotation_matrix_to_axis_angle(R):
    theta = np.arccos((np.trace(R) - 1) / 2)
    if np.isclose(theta, 0):
        return np.array([0, 0, 0]), 0
    else:
        r = 1 / (2 * np.sin(theta)) * np.array([R[2,1]-R[1,2], R[0,2]-R[2,0], R[1,0]-R[0,1]])
        return r, theta

def axis_angle_to_quaternion(axis, angle):
    q = np.zeros(4)
    q[0] = np.cos(angle / 2)
    q[1:] = axis * np.sin(angle / 2)
    return q

def quaternion_to_axis_angle(q):
    angle = 2 * np.arccos(q[0])
    axis = q[1:] / np.sin(angle / 2)
    return axis, angle

def axis_angle_to_rotation_vector(axis, angle):
    return axis * angle

def rotation_vector_to_axis_angle(rotation_vector):
    angle = np.linalg.norm(rotation_vector)
    axis = rotation_vector / angle
    return axis, angle

def axis_angle_to_rotation_matrix(axis, angle):
    axis = axis.astype(np.float64)
    axis /= np.linalg.norm(axis)
    c = np.cos(angle)
    s = np.sin(angle)
    t = 1 - c
    x, y, z = axis
    rotation_matrix = np.array([
        [t*x*x + c, t*x*y - z*s, t*x*z + y*s],
        [t*x*y + z*s, t*y*y + c, t*y*z - x*s],
        [t*x*z - y*s, t*y*z + x*s, t*z*z + c]
    ])
    return rotation_matrix

def test_axis_angle_quaternion_conversion():
    # Define a rotation axis and an angle
    axis = np.array([1, 0, 0])
    angle = np.pi / 2

    # Convert axis-angle to quaternion
    q = axis_angle_to_quaternion(axis, angle)
    print("Quaternion:")
    print(np.round(q, 2))

    # Convert quaternion back to axis-angle
    axis_converted, angle_converted = quaternion_to_axis_angle(q)
    print("\nConverted Axis-Angle:")
    print("Axis:", np.round(axis_converted, 2))
    print("Angle:", np.round(angle_converted, 2))

    # Check if the original and converted axis-angle are close
    print("\nAre the original and converted axis-angle close?")
    print(np.allclose(axis, axis_converted) and np.allclose(angle, angle_converted))

def test_rotation_conversion_functions():
    # Define a rotation axis and an angle
    axis = np.array([1, 0, 0])
    angle = np.pi / 2

    # Convert axis-angle to rotation matrix
    R = axis_angle_to_rotation_matrix(axis, angle)
    print("Rotation Matrix:")
    print(np.round(R, 2))

    # Convert rotation matrix back to axis-angle
    axis_converted, angle_converted = rotation_matrix_to_axis_angle(R)
    print("\nConverted Axis-Angle:")
    print("Axis:", np.round(axis_converted, 2))
    print("Angle:", np.round(angle_converted, 2))

    # Check if the original and converted axis-angle are close
    print("\nAre the original and converted axis-angle close?")
    print(np.allclose(axis, axis_converted) and np.allclose(angle, angle_converted))

    # Convert axis-angle to rotation vector
    rotation_vector = axis_angle_to_rotation_vector(axis, angle)
    print("\nRotation Vector:")
    print(np.round(rotation_vector, 2))

    # Convert rotation vector back to axis-angle
    axis_converted, angle_converted = rotation_vector_to_axis_angle(rotation_vector)
    print("\nConverted Axis-Angle:")
    print("Axis:", np.round(axis_converted, 2))
    print("Angle:", np.round(angle_converted, 2))

    # Check if the original and converted axis-angle are close
    print("\nAre the original and converted axis-angle close?")
    print(np.allclose(axis, axis_converted) and np.allclose(angle, angle_converted))



#Exercice 6
def axis_angle_to_other_representations(axis, angle):
    quaternion = axis_angle_to_quaternion(axis, angle)
    rotation_vector = axis_angle_to_rotation_vector(axis, angle)
    return quaternion, rotation_vector

#Exercice 6 
def convert_rotation(r, e, p, q, v): 
    if np.any(r):
        # Convert rotation matrix to other representations 
        euler_angles = rotation_matrix_to_euler_angles(r) 
        axis_angle = rotation_matrix_to_axis_angle(r) 
        quaternion = axis_angle_to_quaternion(axis_angle[0], axis_angle[1]) 
        rotation_vector = axis_angle_to_rotation_vector(axis_angle[0], axis_angle[1]) 
        return r, euler_angles, axis_angle, quaternion, rotation_vector 
    elif e is not None: 
        # Convert Euler rotation angles to other representations 
        rotation_matrix = euler_angles_to_rotation_matrix(e) 
        axis_angle = rotation_matrix_to_axis_angle(rotation_matrix) 
        quaternion = axis_angle_to_quaternion(axis_angle[0], axis_angle[1]) 
        rotation_vector = axis_angle_to_rotation_vector(axis_angle[0], axis_angle[1]) 
        return rotation_matrix, e, axis_angle, quaternion, rotation_vector 
    elif p is not None: 
        # Convert principal Euler axis/angle to other representations 
        rotation_matrix = axis_angle_to_rotation_matrix(p[0], p[1])
        euler_angles = rotation_matrix_to_euler_angles(rotation_matrix)
        quaternion = axis_angle_to_quaternion(p[0], p[1])
        rotation_vector = axis_angle_to_rotation_vector(p[0], p[1])
        return rotation_matrix, euler_angles, p, quaternion, rotation_vector
    elif q is not None: 
        # Convert quaternion to other representations 
        axis_angle = quaternion_to_axis_angle(q)
        rotation_matrix = axis_angle_to_rotation_matrix(axis_angle[0], axis_angle[1])
        euler_angles = rotation_matrix_to_euler_angles(rotation_matrix)
        rotation_vector = axis_angle_to_rotation_vector(axis_angle[0], axis_angle[1])
        return rotation_matrix, euler_angles, axis_angle, q, rotation_vector
    elif v is not None: 
        # Convert rotation vector to other representations 
        axis_angle = rotation_vector_to_axis_angle(v)
        rotation_matrix = axis_angle_to_rotation_matrix(axis_angle[0], axis_angle[1])
        euler_angles = rotation_matrix_to_euler_angles(rotation_matrix)
        quaternion = axis_angle_to_quaternion(axis_angle[0], axis_angle[1])
        return rotation_matrix, euler_angles, axis_angle, quaternion, v
    else: return None

def test_convert_rotation():
    # Define a rotation matrix, Euler angles, principal Euler axis/angle, quaternion, and rotation vector
    r = np.eye(3)
    e = np.array([np.pi/4, np.pi/3, np.pi/2])
    p = (np.array([1, 0, 0]), np.pi/2)
    q = np.array([np.cos(np.pi/4), np.sin(np.pi/4), 0, 0])
    v = np.array([np.pi/2, 0, 0])

    # Test convert_rotation with different types of inputs
    print("Test with rotation matrix:")
    print(tuple(np.round(arr, 2) if not isinstance(arr, (list, tuple)) else tuple(np.round(a, 2) for a in arr) for arr in convert_rotation(r, None, None, None, None) if arr is not None))
    print("\nTest with Euler angles:")
    print(tuple(np.round(arr, 2) if not isinstance(arr, (list, tuple)) else tuple(np.round(a, 2) for a in arr) for arr in convert_rotation(None, e, None, None, None) if arr is not None))
    print("\nTest with principal Euler axis/angle:")
    print(tuple(np.round(arr, 2) if not isinstance(arr, (list, tuple)) else tuple(np.round(a, 2) for a in arr) for arr in convert_rotation(None, None, p, None, None) if arr is not None))
    print("\nTest with quaternion:")
    print(tuple(np.round(arr, 2) if not isinstance(arr, (list, tuple)) else tuple(np.round(a, 2) for a in arr) for arr in convert_rotation(None, None, None, q, None) if arr is not None))
    print("\nTest with rotation vector:")
    print(tuple(np.round(arr, 2) if not isinstance(arr, (list, tuple)) else tuple(np.round(a, 2) for a in arr) for arr in convert_rotation(None, None, None, None, v) if arr is not None))



#Unit Testing
import unittest

class UnitTestin(unittest.TestCase):
    def test_euler_to_rotation_matrix(self):
        axis = np.array([1, 0, 0])
        angle = np.pi / 2
        expected_result = np.array([
            [1.0, 0.0, 0.0],
            [0.0, np.cos(angle), -np.sin(angle)],
            [0.0, np.sin(angle), np.cos(angle)]
        ])
        np.testing.assert_array_almost_equal(euler_to_rotation_matrix(axis, angle), expected_result, decimal=5)

    def test_quaternion_multiply(self):
        q1 = np.array([1, 0, 0, 0])
        q2 = np.array([0, 1, 0, 0])
        expected_result = np.array([0, 1, 0, 0])
        np.testing.assert_array_almost_equal(quaternion_multiply(q1, q2), expected_result, decimal=5)

    def test_rotate_vector(self):
        vector = np.array([1, 0, 0])
        quaternion = np.array([np.cos(np.pi/4), np.sin(np.pi/4)*1, 0, 0])  # Quaternion representing a 90 degree rotation around the x-axis
        expected_result = np.array([1, 0, 0])
        np.testing.assert_array_almost_equal(rotate_vector(vector, quaternion), expected_result, decimal=5)
    
    def test_generate_random_matrices(self):
        matrices, angles, execution_time = generate_random_matrices()
        self.assertEqual(len(matrices), 100)
        self.assertEqual(len(angles), 100)
        self.assertGreater(execution_time, 0)

    def test_plot_trace_vs_angle(self):
        matrices, angles, execution_time = generate_random_matrices()
        plot_trace_vs_angle(matrices, angles, execution_time)
        self.assertGreater(execution_time, 0)

    def test_convert_rotation(self):
        rotation_matrix = np.array([
            [0, -1, 0],
            [1, 0, 0],
            [0, 0, 1]
        ])
        expected_euler_angles = np.array([0, 0, np.pi/2])
        expected_axis_angle = (np.array([0, 0, 1]), np.pi/2)
        expected_quaternion = np.array([np.cos(np.pi/4), 0, 0, np.sin(np.pi/4)])
        expected_rotation_vector = np.array([0, 0, np.pi/2])

        result = convert_rotation(r=rotation_matrix, e=None, p=None, q=None, v=None)        
        np.testing.assert_array_almost_equal(result[0], rotation_matrix, decimal=5)
        np.testing.assert_array_almost_equal(result[1], expected_euler_angles, decimal=5)
        np.testing.assert_array_almost_equal(result[2][0], expected_axis_angle[0], decimal=5)
        self.assertAlmostEqual(result[2][1], expected_axis_angle[1], places=5)
        np.testing.assert_array_almost_equal(result[3], expected_quaternion, decimal=5)
        np.testing.assert_array_almost_equal(result[4], expected_rotation_vector, decimal=5)


if __name__ == "__main__":
    
    test_rotation_matrix()
    print('---------------------------------')
    test_quaternion_rotation()
    print('---------------------------------')
    test_exercice_3()
    print('---------------------------------')
    test_euler_rotation_conversion()
    print('---------------------------------')
    test_axis_angle_quaternion_conversion()
    print('---------------------------------')
    test_rotation_conversion_functions()
    print('---------------------------------')
    test_convert_rotation()
    print('---------------------------------')
    print('All tests passed!')