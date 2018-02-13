import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf



x = 2
y = 3
op1 = tf.add(x, y)
op2 = tf.multiply(x, y)
op3 = tf.pow(op2, op3)
with tf.Session as sess:
	op3 = sess.run(op3)
print (op3)
'''
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
