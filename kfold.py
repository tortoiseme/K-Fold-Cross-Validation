import random
class CrossValidation:
    def __init__(self, n_folds):
        self.n_folds = n_folds

    def __generate_folds(self, X):
        folds = []
        indices = list(range(0, len(X)))
        fold_size = len(X) // self.n_folds
        for i in range(self.n_folds):
            fold = []
            while(len(fold)< fold_size):
                idx  = random.randrange(0, len(indices))
                fold.append(indices.pop(idx))                
            folds.append(fold)
        return folds

    def split(self, X):  
        """
        Args:
            X (object): [Input data]

        Yields:
            Tuple: [training and test set indices for the split]
        """          
        folds = self.__generate_folds(X)        
        for i in range(self.n_folds):
            test_fold = folds[i] 
            train_folds = [val for idx, fold in enumerate(folds) for val in fold if idx !=i]
            yield (train_folds, test_fold)

         