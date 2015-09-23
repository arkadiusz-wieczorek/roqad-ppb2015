class Statistics(object):
    """
    Represents statistics on how good the hypothesis was
    """

    def __init__(self, tp=0, tn=0, fn=0, fp=0, common_clusters_no=0,
                 common_cluster_devices_nos=None, pred_cluster_devices_nos=None, true_cluster_devices_nos=None):
        """
        Creates new stats

        :param tp: true positives for connections between devices
        :type tp: int
        :param tn: true negatives for connections between devices
        :type tn: int
        :param fn: false negatives for connections between devices
        :type fn: int
        :param fp: false positives for connections between devices
        :type fp: int
        :param common_clusters_no: number of exactly the same clusters in predicted and gold standard graph
        :type common_clusters_no: int
        :param common_cluster_devices_nos: matrix of common devices number for each pair of predicted and gs clusters.
        Row index of this matrix represents index of predicted cluster, column index represents index of gs cluster.
        :type common_cluster_devices_nos: numpy.ndarray
        :param pred_cluster_devices_nos: list of devices number for each predicted cluster
        :type pred_cluster_devices_nos: list
        :param true_cluster_devices_nos: list of devices number for each cluster in gold standard graph
        :type true_cluster_devices_nos: list
        """
        self.tp = float(tp)
        self.tn = float(tn)
        self.fn = float(fn)
        self.fp = float(fp)
        self.all = self.tp + self.tn + self.fn + self.fp

        self.common_clusters_no = float(common_clusters_no)
        self.common_devices_nos = common_cluster_devices_nos
        self.pred_devices_nos = pred_cluster_devices_nos
        self.true_devices_nos = true_cluster_devices_nos

    def prec(self):
        # High precision means that an algorithm returned substantially more relevant results than irrelevant
        den = self.tp + self.fp
        return self.tp / den if den else 0

    def recall(self):
        # High recall means that an algorithm returned most of the relevant results
        den = self.tp + self.fn
        return self.tp / den if den else 0

    def f1(self):
        # F1 score can be interpreted as a weighted average of the precision and recall, where an F1 score reaches its
        # best value at 1 and worst score at 0.
        den = self.prec() + self.recall()
        return 2 * self.prec() * self.recall() / den if den else 0

    def accuracy(self):
        # Accuracy is the proportion of true results (both true positives and true negatives) among the total number
        # of cases examined.
        return (self.tp + self.tn) / self.all if self.all else 0

    def tp_rate(self):
        return (self.tp / self.all) * 100 if self.all else 0

    def fp_rate(self):
        return (self.fp / self.all) * 100 if self.all else 0

    def fn_rate(self):
        return (self.fn / self.all) * 100 if self.all else 0

    def tn_rate(self):
        return (self.tn / self.all) * 100 if self.all else 0

    def cluster_prec(self):
        pred_clusters_no = len(self.pred_devices_nos)
        if self.common_clusters_no > pred_clusters_no:
            raise ValueError('The number of common clusters should be less than number of predicted clusters')
        return self.common_clusters_no / pred_clusters_no if pred_clusters_no else 0

    def cluster_recall(self):
        true_clusters_no = len(self.true_devices_nos)
        if self.common_clusters_no > true_clusters_no:
            raise ValueError('The number of common clusters should be less than number of true clusters')
        return self.common_clusters_no / true_clusters_no if true_clusters_no else 0

    def cluster_f1(self):
        p = self.cluster_prec()
        r = self.cluster_recall()
        denominator = (p + r)
        return 2 * p * r / denominator if denominator else 0

    def closest_cluster_prec(self):
        clusters_sims_sum = 0
        for pred_cluster_idx in xrange(len(self.pred_devices_nos)):
            max_sim_td_no = None
            for true_cluster_idx in xrange(len(self.true_devices_nos)):
                clusters_jaccard_sim = self._calculate_jaccard_clusters_similarity(pred_cluster_idx, true_cluster_idx)
                max_sim_td_no = max(max_sim_td_no, clusters_jaccard_sim)
            if max_sim_td_no:
                clusters_sims_sum += max_sim_td_no
        return clusters_sims_sum / len(self.pred_devices_nos) if len(self.pred_devices_nos) else 0

    def closest_cluster_recall(self):
        clusters_sims_sum = 0
        for true_cluster_idx in xrange(len(self.true_devices_nos)):
            max_sim_pd_no = None
            for pred_cluster_idx in xrange(len(self.pred_devices_nos)):
                clusters_jaccard_sim = self._calculate_jaccard_clusters_similarity(pred_cluster_idx, true_cluster_idx)
                max_sim_pd_no = max(max_sim_pd_no, clusters_jaccard_sim)
            if max_sim_pd_no:
                clusters_sims_sum += max_sim_pd_no
        return clusters_sims_sum / len(self.true_devices_nos) if len(self.true_devices_nos) else 0

    def closest_cluster_f1(self):
        p = self.closest_cluster_prec()
        r = self.closest_cluster_recall()
        denominator = (p + r)
        return 2 * p * r / denominator if denominator else 0

    def _calculate_jaccard_clusters_similarity(self, pred_cluster_idx, true_cluster_idx):
        comm_devices_number = self.common_devices_nos[pred_cluster_idx][true_cluster_idx]
        pred_devices_number = self.pred_devices_nos[pred_cluster_idx]
        true_devices_number = self.true_devices_nos[true_cluster_idx]
        if comm_devices_number > pred_devices_number:
            raise ValueError('The number of common devices for pair of true and predicted clusters should '
                             'be less than the number of devices only in predicted cluster')
        if comm_devices_number > true_devices_number:
            raise ValueError('The number of common devices for pair of true and predicted clusters should '
                             'be less than the number of devices only in true cluster')
        return float(comm_devices_number) / (pred_devices_number + true_devices_number - comm_devices_number) if (pred_devices_number + true_devices_number - comm_devices_number) else 0 

