#!/usr/bin/env python

import add_user_id_to_choosen_dataset as add_id
import cartesian_product as cart_prod

dataset_with_id = add_id.addUserID('../Data/RownowazoneDane.csv', '../roq-ad-data-set/learning-set/labels.csv', 1)

cart_prod.cartesianProduct(dataset_with_id)

print "ready!"