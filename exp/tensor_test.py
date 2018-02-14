import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
#Visualize it with TensorBoard
a = tf.constant(2)
b = tf.constant(3)
x = tf.add(a, b)
#Create the summary writer after graph definition and before running session
writer = tf.summary.FileWriter('./graphs', tf.get_default_graph())
with tf.Session() as sess:
  # writer = tf.summary.FileWriter('./graphs', sess.graph)
  print(sess.run(x))
writer.close()
'''
#First tensorflow program
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