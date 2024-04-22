from typing import List, Tuple


from typing import List

from typing import List

def get_confusion_matrix(
    y_true: List[int], y_pred: List[int], num_classes: int,
) -> List[List[int]]:
    """
    Generate a confusion matrix in the form of a list of lists.

    :param y_true: a list of ground truth values
    :param y_pred: a list of prediction values
    :param num_classes: number of supported classes

    :return: confusion matrix
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Invalid input shapes!")

    if any(label >= num_classes for label in y_true + y_pred):
        raise ValueError("Invalid prediction classes!")

    confusion_matrix = [[0] * num_classes for _ in range(num_classes)]
    for true, pred in zip(y_true, y_pred):
        confusion_matrix[true][pred] += 1
    return confusion_matrix


from typing import List, Tuple

def get_quality_factors(
    y_true: List[int],
    y_pred: List[int],
) -> Tuple[int, int, int, int]:
    """
    Calculate True Negative, False Positive, False Negative, and True Positive
    metrics based on the ground truth and predicted lists.

    :param y_true: a list of ground truth values
    :param y_pred: a list of prediction values

    :return: a tuple of TN, FP, FN, TP
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Length of y_true and y_pred must be the same!")

    tn, fp, fn, tp = 0, 0, 0, 0
    for true, pred in zip(y_true, y_pred):
        if true == pred:
            if true == 0:
                tn += 1
            else:
                tp += 1
        else:
            if true == 0:
                fp += 1
            else:
                fn += 1
    return tn, fp, fn, tp





def accuracy_score(y_true: List[int], y_pred: List[int]) -> float:
    """
    Calculate the accuracy for given lists.
    :param y_true: a list of ground truth values
    :param y_pred: a list of prediction values

    :return: accuracy score
    """
    tn, fp, fn, tp = get_quality_factors(y_true, y_pred)
    total_samples = len(y_true)

    if total_samples == 0:
        return 0.0

    accuracy_value = (tp + tn) / total_samples
    return accuracy_value

def precision_score(y_true: List[int], y_pred: List[int]) -> float:
    """
    Calculate the precision for given lists.
    :param y_true: a list of ground truth values
    :param y_pred: a list of prediction values

    :return: precision score
    """
    tn, fp, fn, tp = get_quality_factors(y_true, y_pred)

    if tp + fp == 0:
        return 0.0

    precision_value = tp / (tp + fp)
    return precision_value


def recall_score(y_true: List[int], y_pred: List[int]) -> float:
    """
    Calculate the recall for given lists.
    :param y_true: a list of ground truth values
    :param y_pred: a list of prediction values

    :return: recall score
    """
    tn, fp, fn, tp = get_quality_factors(y_true, y_pred)

    if tp + fn == 0:
        return 0.0

    recall_value = tp / (tp + fn)
    return recall_value


def f1_score(y_true: List[int], y_pred: List[int]) -> float:
    """
    Calculate the F1-score for given lists.
    :param y_true: a list of ground truth values
    :param y_pred: a list of prediction values

    :return: F1-score
    """
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)

    if precision + recall == 0:
        return 0.0

    f1_score_value = 2 * (precision * recall) / (precision + recall)
    return f1_score_value