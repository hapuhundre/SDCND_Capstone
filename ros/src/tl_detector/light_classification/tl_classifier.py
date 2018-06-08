from styx_msgs.msg import TrafficLight

import os


class TLClassifier(object):
    def __init__(self):
        #TODO load classifier
        # pass
        num_classes = 3
        pwd = os.path.dirname(os.path.realpath(__file__))
        model_path = os.path.join(pwd, '')
        labeltxt_path = os.path.join(pwd, '')

        self.img = None
        self.category_dict =  { 1:{'name':'red', 'id':1}, 
                                2:{'name':'yellow', 'id':2}, 
                                3:{'name':'green', 'id':3}}
        
        self.sess = tf.Session()




    def get_classification(self, image):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)

        """
        #TODO implement light color prediction
        
        traffic_light = TrafficLight.UNKNOWN
        min_threshold = 0.5

        with self.d_graph.as_default():
            expanded_img = np.expand_dims(image, axis=0)
            (boxes, scores, classes, num) = self.sess.run([self.detection_boxes,self.detection_scores, 
                                                           self.detection_classes,self.detection_num],
                                                           feed_dict={self.img_tensor: expanded_img})
            boxes = np.squeeze(boxes)
            classes = np.squeeze(classes).astype(np.int32)
            scores = np.squeeze(scores)

            for idx in range(boxes.shape[0]):
                if scores[idx] > min_threshold:
                    prediction = self.category_dict[classes[idx]]['name']
              
                    if prediction == 'red':
                        traffic_light = TrafficLight.RED
                    elif prediction == 'green':
                        traffic_light = TrafficLight.GREEN
                    elif prediction == 'yellow':
                        traffic_light = TrafficLight.YELLOW
        
        return traffic_light
