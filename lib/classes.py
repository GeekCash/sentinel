#!/usr/bin/env python

# NGM/TODO: this entire file could be replace with an ORM and implementation of
# 'superblock' and 'proposal'
#
# NGM: DONE - 2016-08-20 19:22 UTC
#

"""

    Proposal Object

    - These objects are created when a user would like to be paid by the network via superblock.

        proposal --create --proposal_name="beer-reimbursement"
        --description_url="www.dashwhale.org/p/beer-reimbursement"
        --start_date="2017/1/1"
        --end_date="2017/6/1"
        --payment_address="Xy2LKJJdeQxeyHrn4tGDQB8bjhvFEdaUv7"'

    """

"""

    Superblock

        superblock --create --start_date="2017/1/1"
        --payments="[Addr1, amount],[Addr2, amount],[Addr3, amount]"

        --

        object structure:

        {
            'subtype': 'superblock',
            'superblock_name': 'sb1803405',
            'governance_object_id': 0,
            'event_block_height': '',
            'type': -1
            'payment_addresses': 'yNaE8Le2MVwk1zpwuEKveTMCEQHVxdcfCS',
            'payment_amounts': '100',
        }

    """
