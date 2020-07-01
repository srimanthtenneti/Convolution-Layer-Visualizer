class Conv_layervis(nn.Module):
    def __init__(self,layer,img):
        super(layervis , self).__init__()
         
        self.layer = layer
        self.img = img
        self.weights = self.layer.weight.data # Load the weights
        
        self.w = self.weights.numpy()
        
        self.fig = plt.figure(figsize = (30 , 10))

        self.columns = 5*2
        self.rows = 2

        for i in range(self.columns * self.rows):
            self.fig.add_subplot(self.rows , self.columns , i+1)
            if(i%2 == 0):
                plt.imshow(self.w[int(i/2)][0] , cmap = 'gray')
            else:
                self.c = cv2.filter2D(self.img , -1 , self.w[int((i-1)/2)][0])
                plt.imshow(self.c , cmap = 'gray')

        