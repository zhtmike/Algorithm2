from csv import reader
from itertools import accumulate


class Assign1(object):
    """
    Assignment 1
    """

    @staticmethod
    def read_txt(txt_name):
        """
        Read the first line as the total number,
        Read the remaining part as a list of (weight, length).
        :param txt_name: (str) location of the txt
        :return: (list) list of (weight, length)
        """
        job_list = []
        with open(txt_name, 'r') as csv_file:
            total_num = int(csv_file.readline())
            remain = reader(csv_file, delimiter=' ')
            for row in remain:
                job_list.append([int(x) for x in row])
        assert total_num == len(job_list)
        return job_list

    def question_one(self, txt_name):
        """
        Minimize the completion time by sorting the job according to weight - length
        :param txt_name: (str) location of the txt
        :return: total sum of weighted completion time
        """
        job_list = self.read_txt(txt_name)
        # Sorting the job by (first, weight - length; second, weight) reversely
        sorted_list = sorted(job_list, key=lambda info: (info[0] - info[1], info[0]), reverse=True)
        # Accumulate the completion time
        completion_time = list(accumulate([item[1] for item in sorted_list]))
        # Compute the weighted completion time
        weighted_completion_time = [sorted_list[i][0] * completion_time[i] for i in range(len(sorted_list))]
        return sum(weighted_completion_time)

    def question_two(self, txt_name):
        """
        Minimize the completion time by sorting the job according to weight / length
        :param txt_name: (str) location of the txt
        :return: total sum of weighted completion time
        """
        job_list = self.read_txt(txt_name)
        # Sorting the job by (first, weight - length; second, weight) reversely
        sorted_list = sorted(job_list, key=lambda info: info[0] / info[1], reverse=True)
        # Accumulate the completion time
        completion_time = list(accumulate([item[1] for item in sorted_list]))
        # Compute the weighted completion time
        weighted_completion_time = [sorted_list[i][0] * completion_time[i] for i in range(len(sorted_list))]
        return sum(weighted_completion_time)


if __name__ == '__main__':
    assign1 = Assign1()
    text_path = 'data/_642c2ce8f3abe387bdff636d708cdb26_jobs.txt'
    print(assign1.question_one(text_path))
    print(assign1.question_two(text_path))
