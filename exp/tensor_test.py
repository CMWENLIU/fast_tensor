import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
import numpy as np

#------------------TF Variables
print('\nTensorflow integrate seamless with Numpy:\n',tf.int32 == np.int32)
tensor_numpy = tf.ones([2, 2], np.float32)
with tf.Session() as sess:
	a = sess.run(tensor_numpy)
	print (type(a), a)
W = tf.Variable(tf.zeros([7,10]))
e = tf.zeros([3, 5], tf.float32)
W1 = tf.Variable(10)
assign_op = W1.assign(100)
my_var = tf.Variable(2, name = 'my_var')
my_var_times_two = my_var.assign(2 * my_var)
print (my_var)
with tf.Session() as sess:
	sess.run(W.initializer)
	sess.run(W1.initializer)
	sess.run(assign_op)
	sess.run(my_var.initializer)
	sess.run(my_var_times_two)
	print(my_var.eval())
	print(my_var_times_two.eval())
	print (W1)
	print (W1.eval())
	print (W.eval())
	print (sess.run(e))
print(W)
print(e)
'''
#-------------------Constants, Sequences, Variables, Ops
a = tf.constant([2, 8], name = 'a')
b = tf.constant([[0, 1], [2, 3]], name = 'b')
x = tf.multiply(a, b, name = 'mul')
c = tf.zeros([3, 5], tf.float64)
d = tf.zeros_like(b, tf.float32)
e = tf.ones_like(a,)
f = tf.fill([4, 6], 8, name = 'numbers_8')
lin_space = tf.lin_space(10.0, 13.0, 10)
range_num = tf.range(3, 18, 5)
with tf.Session() as sess:
	print('\nThis is tensor x:\n', sess.run(x))
	print('\nThis is tensor c:\n', sess.run(c))
	print('\nThis is tensor d:\n', sess.run(d))
	print('\nThis is tensor e:\n', sess.run(e))
	print('\nThis is tensor f:\n', sess.run(f))
	print('\nThis is tensor lin_space:\n', sess.run(lin_space))
	print('\nThis is tensor range_number:\n', sess.run(range_num))

#----------------------Visualize it with TensorBoard
a = tf.constant(2)
b = tf.constant(3)
x = tf.add(a, b)
#Create the summary writer after graph definition and before running session
writer = tf.summary.FileWriter('./graphs', tf.get_default_graph())
with tf.Session() as sess:
  # writer = tf.summary.FileWriter('./graphs', sess.graph)
  print(sess.run(x))
writer.close()
#---------------------First tensorflow program
a = tf.constant(2)
b = tf.constant(3)
x = tf.add(a, b)
with tf.Session() as sess:
  print(sess.run(x))
#---------------------Add operators to Graph
g = tf.Graph()
with g.as_default():
  x = tf.add(3, 5)
sess = tf.Session(graph=g)
with tf.Session() as sess:
  sess.run(x)
#---------------------Put part of graph to specific CPU or GPU
#Create a graph.
with tf.device('/cpu:1'):
  a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], name = 'a')
  b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], name = 'b')
  c = tf.multiply(a, b)
#Create a session with log_device_placement set to True.
sess = tf.Session(config = tf.ConfigProto(log_device_placement = True))
#run the op
print(sess.run(c))
#-------------------------------
x = 2
y = 3
add_op = tf.add(x, y)
mul_op = tf.multiply(x, y)
useless = tf.multiply(x, add_op)
pow_op = tf.pow(add_op, mul_op)
with tf.Session() as sess:
  z, useful = sess.run([pow_op, useless])
print(z, useful)

#----------------------------------
x = 2
y = 3
op1 = tf.add(x, y)
print (op1)
op2 = tf.multiply(x, y)
op3 = tf.pow(op1, op2)
with tf.Session() as sess:
	op3 = sess.run(op3)
print (op3)
#--------------------------------------
state = tf.Variable(0, name = "counter")
one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)

init_op = tf.global_variables_initializer()

with tf.Session() as sess:
	sess.run(init_op)
	print (sess.run(state))
	for _ in range(3):
		sess.run(update)
		print (sess.run(state))

#---------------------------------
input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(5.0)
intermed = tf.add(input2, input3)
mul = tf.multiply(input1, intermed)

with tf.Session() as sess:
	result = sess.run(mul)
	print (result)
#----------------------------------


input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.multiply(input1, input2)

with tf.Session() as sess:
	result = sess.run([output], feed_dict = {input1: [7.], input2: [2.]})
	print (result)
'''
