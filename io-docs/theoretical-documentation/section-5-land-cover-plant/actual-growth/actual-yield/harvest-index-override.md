# Harvest Index Override

&#x20;                In the plant and harvest only operations (.mgt), the model allows the user to specify a target harvest index. The target harvest index set in a plant operation is used when the yield is removed using a harvest/kill operation. The target harvest index set in a harvest only operation is used only when that particular harvest only operation is executed.

&#x20;           When a harvest index override is defined, the override value is used in place of the harvest index calculated by the model in the yield calculations. Adjustments for growth stage and water deficiency are not made.

&#x20;             $$HI_{act}=HI_{trg}$$                                                                                                 5:3.3.3

where $$HI_{act}$$ is the actual harvest index and $$HI_{trg}$$ is the target harvest index.
