class Distribution:
    def __init__(self, mu=0, sigma=1):
        """ Generic distribution class for calculating and visualizing a probablity distribution.
        
        Args:
            mean (float) representing the mean value of the distribution
            stdev (float) representing the standard deviation of the distribution

            data_list = (list of floats) a list of floats extracted from the data file
        """

        self.mean = mu
        self.stdev = sigma

        self.data = []

        def read_data_list(self, file_name):
            """A function to read data from teh textfile. The text file should have one number (float) per line
            The number are stored in the data attribute.

            Args:
                file_name (string) : name of the file to read from

            Returns:
                None

            """
            with open(file_name) as file:
                data_list = []
                line = file.readline()
                while line:
                    data_list.append(len(line))
                    line = file.readline()
            file.close()
            self.data = data_list
