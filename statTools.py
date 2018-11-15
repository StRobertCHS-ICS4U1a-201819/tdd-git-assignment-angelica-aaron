def mode(num_list):

   try:
       max_occures = 0
       current_occures = 0
       mode_list = []
       if not num_list:
           return []
       prev_num = num_list[0]
       i = 0
       while i < len(num_list):
           if num_list[i] == prev_num:
               current_occures += 1
           else:
               if current_occures > max_occures:
                   max_occures = current_occures
                   mode_list = [num_list[i - 1]]
               elif current_occures > max_occures:
                   mode_list.append(num_list[i - 1])
               current_occures = 1  # reset occurrences
           prev_num = num_list[i]
           i = + 1